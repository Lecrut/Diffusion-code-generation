import unicodedata
def sort_unicode_collation(items):
    return sorted(items, key=lambda x: unicodedata.normalize('NFKC', x))
if __name__ == '__main__':
    sample_data = ['café', 'Zürich', 'naïve', '日本語', 'αβγδ']
    result = sort_unicode_collation(sample_data)
    print(result)