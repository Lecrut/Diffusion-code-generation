def count_vowels(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    try:
        print(count_vowels(sample_string))
    except Exception as e:
        print(f"Error: {e}")