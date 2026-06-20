status_map = {
    True: 'Pass',
    False: 'Fail'
}

def check_status(score):
    return status_map[score >= 60]

if __name__ == '__main__':
    print(check_status(55))
    print(check_status(70))