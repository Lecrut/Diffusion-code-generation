def vowel_count_generator(input_string):
    for char in input_string:
        count = 0
        lower_char = char.lower()
        if 'a' in lower_char:
            count += 1
        if 'e' in lower_char:
            count += 1
        if 'i' in lower_char:
            count += 1
        if 'o' in lower_char:
            count += 1
        if 'u' in lower_char:
            count += 1
        yield count
def calculate_total_vowel_count(generator):
    total = 0
    for count in generator:
        total += count
    return total
if __name__ == '__main__':
    sample_string = "Programming"
    vowel_counts = vowel_count_generator(sample_string)
    total_sum = calculate_total_vowel_count(vowel_counts)
    print(f"Input String: {sample_string}")
    print(f"Total Vowel Count Sum: {total_sum}")