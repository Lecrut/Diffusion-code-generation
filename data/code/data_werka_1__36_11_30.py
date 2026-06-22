if __name__ == '__main__':
    sample_strings = ["hello", "world", "optimization", ""]
    for original in sample_strings:
        try:
            reversed_str = reverse_string(original)
            print(f"Original: {original}, Reversed: {reversed_str}")
        except ValueError as e:
            print(e)