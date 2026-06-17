def main():
    sample_input = "Hello World This Is A Test String"
    words_list = sample_input.split()
    result_string = "".join(word[0] for word in words_list)
    print(result_string)
if __name__ == '__main__':
    main()