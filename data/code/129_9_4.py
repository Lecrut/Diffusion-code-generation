def custom_sort(string_list):
    letter_ranks = {chr(ord('A') + i): i for i in range(26)}
    def sort_key(s):
        if s:
            return letter_ranks[s[0].upper()]
        return 26
    return sorted(string_list, key=sort_key)
if __name__ == '__main__':
    data = ["Banana", "Apple", "Cat", "Ant", "Ball", "Dog", "Apricot"]
    sorted_data = custom_sort(data)
    print(sorted_data)