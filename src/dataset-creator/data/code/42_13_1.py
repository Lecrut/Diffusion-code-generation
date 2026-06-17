import unicodedata
def sort_unicode_collation(data):
    return sorted(data, key=lambda x: unicodedata.normalize('NFKC', x))
if __name__ == '__main__':
    sample_data = ['café', 'Zürich', 'naïve', '日本語', 'مرحبا']
    result = sort_unicode_collation(sample_data)
    print(result)