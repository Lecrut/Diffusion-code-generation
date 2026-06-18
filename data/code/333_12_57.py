def main():
    user_input = "Hello World Python Programming"
    words_list = user_input.split()
    result_string = "".join(word[0] for word in words_list)
    print(result_string)
if __name__ == '__main__':
    main()