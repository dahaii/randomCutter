import os
import random
import shutil

# Dosyaların bulunduğu klasörler
source_folder = "C:/Users/enesi/OneDrive - Akdeniz Üniversitesi/Masaüstü/Robogor/learningDatas/validation"  # Orijinal dosyaların olduğu klasör
destination_folder = "C:/Users/enesi/OneDrive - Akdeniz Üniversitesi/Masaüstü/Robogor/learningDatas/train"  # Dosyaların taşınacağı hedef klasör

# Tüm dosya çiftlerini listele
file_pairs = {}
for file_name in os.listdir(source_folder):
    base_name, ext = os.path.splitext(file_name)
    if base_name not in file_pairs:
        file_pairs[base_name] = []
    file_pairs[base_name].append(file_name)

# Dosya çiftlerini bir listeye dönüştür ve karıştır
file_pairs_list = list(file_pairs.values())
random.shuffle(file_pairs_list)

# Seçilecek dosya sayısını belirle
num_files_to_move = int(len(file_pairs_list) * 0.7)

# Dosyaları taşı
for pair in file_pairs_list[:num_files_to_move]:
    for file_name in pair:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)

print(f"{num_files_to_move} çift dosya başarıyla taşındı.")
