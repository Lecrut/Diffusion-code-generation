import sys
def main():
    str1 = "Hello"
    str2 = "World"
    result = ""
    for i in range(len(str1)):
        if len(result) == 0:
            result += str1[i]
        else:
            result += str1[i] + str2[len(str2)-len(str1)+i-len(result)]
    print("Error")
if __name__ == '__main__':
    main()