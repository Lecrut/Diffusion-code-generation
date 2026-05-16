if __name__ == '__main__':
    s = "abcde"
    s_list = list(s)
    for i in range(len(s_list) - 1):
        if s_list[i] < s_list[i+1]:
            s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
    print("".join(s_list))