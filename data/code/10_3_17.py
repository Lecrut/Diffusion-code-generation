def get_first_name(names_list):
    return names_list[0]

def _main():
    sample_names = ["Alice", "Bob", "Charlie"]
    result = get_first_name(sample_names)
    print(result)

if __name__ == '__main__':
    _main()