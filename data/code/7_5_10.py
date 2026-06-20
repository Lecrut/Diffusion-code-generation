def count_special_characters(text):
    special_chars = set("!@#$%^&*()_+-=[]{}|;:',.<>?/`~")
    count = 0
    for char in text:
        if char in special_chars:
            count += 1
    return count, count > 0

if __name__ == "__main__":
    sample_text = "Hello, World! This is a test@123."
    result_count, has_special = count_special_characters(sample_text)
    print(result_count)
    print(has_special)