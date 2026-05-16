def custom_sort(string_list):
    letter_rank = {chr(ord('A') + i): i for i in range(26)}
    def sort_key(s):
        if s:
            return letter_rank[s[0].upper()]
        return 26
    return sorted(string_list, key=sort_key)
if __name__ == '__main__':
    sample_list = ["Banana", "Apple", "Zebra", "Ant", "Bear", "Cat"]
    sorted_list = custom_sort(sample_list)
    print(sorted_list)