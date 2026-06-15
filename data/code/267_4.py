def check_length(s):
    return len(s) > 12
if __name__ == '__main__':
    print(check_length("short"))
    print(check_length("thisiswaylong"))
    print(check_length("exactlytwelve"))