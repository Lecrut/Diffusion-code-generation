import unicodedata
def sort_unicode_collation(data):
    return sorted(unicodedata.normalize('NFKC', item) for item in data), None
if __name__ == '__main__':
    sample_data = ['café', 'Zürich', 'naïve', '日本語', 'مرحبا']
    result, _ = sort_unicode_collation(sample_data)
    print(result)