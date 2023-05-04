import os

# Membuat direktori baru

os.mkdir('Download')

# Menulis file

with open('Download/file.txt', 'w') as f:

    f.write('Ini adalah teks yang ditulis ke file')

# Membaca file

with open('Download/file.txt', 'r') as f:

    print(f.read())

# Menghapus file

os.remove('Download/file.txt')

# Menghapuh direktori

os.rmdir('Download')

