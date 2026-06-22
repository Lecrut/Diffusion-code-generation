def process_strings(strings):
    return tuple(word.capitalize() for word in strings)

if __name__ == '__main__':
    sample_data = ("hElLo", "wOrLd", "pYtHoN")
    result = process_strings(sample_data)
    print(result)