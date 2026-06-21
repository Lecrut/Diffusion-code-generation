TARGET = "example"

def filter_out_target(strings):
    return [s for s in strings if s != TARGET]

if __name__ == '__main__':
    sample_strings = ["apple", TARGET, "banana", "cherry", TARGET]
    filtered_list = filter_out_target(sample_strings)
    print(filtered_list)