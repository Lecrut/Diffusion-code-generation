def process_strings(strings):
    return tuple(s.capitalize() for s in strings)

if __name__ == '__main__':
    sample_data = ("hElLo", "WoRLd", "pYtHon", "tAsK")
    result = process_strings(sample_data)
    print(result)