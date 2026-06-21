sample_strings = ["hello", "world!", "Python3", "2023", "data science"]

filtered_strings = [s for s in sample_strings if s.isalpha()]

if __name__ == '__main__':
    print(filtered_strings)