sample_list = ["hello", "world!", "123", "test123"]

filtered_list = [item for item in sample_list if item.isalpha()]

if __name__ == '__main__':
    print(filtered_list)