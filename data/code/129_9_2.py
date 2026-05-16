def custom_sort(string_list):
    letter_rank = {chr(ord('A') + i): i for i in range(26)}
    def sort_key(s):
        if not s:
            return float('inf')
        first_letter = s[0].upper()
        if 'A' <= first_letter <= 'Z':
            return letter_rank[first_letter]
        return float('inf')
    return sorted(string_list, key=sort_key)
if __name__ == '__main__':
    sample_list = ["Banana", "Apple", "Zebra", "Ant", "Bear", "Cat", "Dog"]
    sorted_list = custom_sort(sample_list)
    print(sorted_list)