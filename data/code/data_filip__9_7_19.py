def normalize_text(data):
    return str(data).strip()

if __name__ == '__main__':
    sample_input_1 = "   hello world   "
    sample_input_2 = "\t\n  python code  \t\n"
    sample_input_3 = "no_spaces"
    
    result_1 = normalize_text(sample_input_1)
    result_2 = normalize_text(sample_input_2)
    result_3 = normalize_text(sample_input_3)
    
    print(result_1)
    print(result_2)
    print(result_3)