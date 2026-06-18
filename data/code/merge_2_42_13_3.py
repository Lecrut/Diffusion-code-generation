import unicodedata
def sort_unicode_alphabetically(items):
    return sorted(
        items, 
        key=lambda x: unicodedata.normalize('NFKC', x)
    )
if __name__ == '__main__':
    sample_data = ['café', 'Zürich', 'naïve', '日本語', 'München', 'αβγ']
    sorted_result = sort_unicode_alphabetically(sample_data)
    print(sorted_result)