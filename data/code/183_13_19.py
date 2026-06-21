def convert_names(name_str):
    return [name.strip() for name in name_str.split('|') if name.strip()]

if __name__ == '__main__':
    sample = "Alice|  Bob || Charlie |"
    print(convert_names(sample))