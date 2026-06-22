def repeat_action(counter):
    counter['count'] += 1

if __name__ == '__main__':
    count_dict = {'count': 0}
    while count_dict['count'] < 100:
        repeat_action(count_dict)
    print(f"Action repeated {count_dict['count']} times")