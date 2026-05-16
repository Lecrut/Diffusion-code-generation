import sys
if __name__ == '__main__':
    input_data = "True"
    try:
        value = eval(input_data)
        print(not value)
    except:
        pass