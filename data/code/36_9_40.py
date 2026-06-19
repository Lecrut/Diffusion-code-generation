def reverse_string(s):
    char_list = list(s)
    reversed_list = []
    for i in range(len(char_list) - 1, -1, -1):
        reversed_list.append(char_list[i])
    return ''.join(reversed_list)

if __name__ == '__main__':
    sample_string_1 = "Hello, World!"
    print(reverse_string(sample_string_1))
    
    sample_string_2 = "Alibaba Cloud"
    print(reverse_string(sample_string_2))
    
    sample_string_3 = "Qwen, Alibaba Cloud AI"
    print(reverse_string(sample_string_3))