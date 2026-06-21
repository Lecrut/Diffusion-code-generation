def check_status(value, threshold, flag):
    if value is None:
        return False
    if value < threshold:
        return False
    if flag:
        return True
    return value >= (threshold * 2)

if __name__ == '__main__':
    val = 20
    thr = 10
    flg = False
    print(check_status(val, thr, flg))