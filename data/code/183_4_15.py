def convert_names_to_list(names_str):
    lines = names_str.split('\n')
    stripped_lines = [line.strip() for line in lines if line.strip()]
    return stripped_lines

if __name__ == '__main__':
    sample_names = """Alice
    
Bob
Charlie"""
    result = convert_names_to_list(sample_names)
    print(result)