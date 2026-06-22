def combine_strings(str1, str2):
    return str1 + str2

if __name__ == '__main__':
    string_combinations = {
        "greeting": ("Hello, ", "World!"),
        "farewell": ("Goodbye, ", "Earth!"),
        "salutation": ("Hi, ", "Universe!")
    }
    
    for key, (part1, part2) in string_combinations.items():
        result = combine_strings(part1, part2)
        print(f"{key}: {result}")