#Python Temel Eğitim Final Projesi
def flatten(n_list):
    flat_list = []
    for item in n_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Eğer item bir listeyse, rekürsif olarak düzleştir
        else:
            flat_list.append(item)  # Aksi halde elemanı doğrudan ekle
    return flat_list

def reverse_nested(n_list):
    reversed_list = []
    for item in reversed(n_list):  # Listenin elemanlarını ters sırada al
        if isinstance(item, list):
            reversed_list.append(reverse_nested(item))  # Eğer item bir listeyse, rekürsif olarak tersine çevir
        else:
            reversed_list.append(item)  # Aksi halde elemanı doğrudan ekle
    return reversed_list
