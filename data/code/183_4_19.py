def convert_names_to_list(names_str):
    return [name.strip() for name in names_str.splitlines() if name.strip()]

if __name__ == '__main__':
    sample_names = """Alice
Bob
Charlie"""
    names_list = convert_names_to_list(sample_names)
    print(names_list)