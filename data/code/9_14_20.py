def strip_string(text):
    return text.strip()

if __name__ == '__main__':
    sample_input = "   Hello World   "
    result = strip_string(sample_input)
    print(result)
    
    sample_input_2 = "\t\n  Python  \t\n"
    result_2 = strip_string(sample_input_2)
    print(result_2)
    
    sample_input_3 = ""
    result_3 = strip_string(sample_input_3)
    print(result_3)
    
    sample_input_4 = "   "
    result_4 = strip_string(sample_input_4)
    print(result_4)