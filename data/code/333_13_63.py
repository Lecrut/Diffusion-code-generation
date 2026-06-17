import sys
def main():
    text = "Hello World Python Programming"
    result_list_comp = [word[0] for word in text.split() if len(word) > 0]
    print("".join(result_list_comp))
if __name__ == '__main__':
    main()