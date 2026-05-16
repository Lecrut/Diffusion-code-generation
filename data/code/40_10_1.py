def process_strings(string_list):
    for s in string_list:
        if s:
            print(s[0])
if __name__ == '__main__':
    data = ["apple", "banana", "cherry", "date", ""]
    process_strings(data)