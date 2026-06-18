import unicodedata
def sort_unicode_collation(data):
    def collator_key(s: str) -> tuple:
        normalized = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8')
        try:
            return ('0', '', sorted(normalized, key=lambda c: ord(c)))
        except Exception:
            return (1, unicodedata.name(s), s)
    data.sort(key=collator_key)
    return data
if __name__ == '__main__':
    sample_list = ["café", "banana", "Zürich", "Москва", "日本語", "αβγ"]
    sorted_list = sort_unicode_collation(sample_list.copy())
    print(sorted_list)