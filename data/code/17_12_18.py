from collections import deque

def create_deque_with_integers():
    d = deque()
    d.append(10)
    d.append(20)
    d.append(30)
    d.append(40)
    d.append(50)
    return d

def pop_last_item(d):
    if not d:
        return None
    return d.pop()

if __name__ == '__main__':
    d = create_deque_with_integers()
    last_item = pop_last_item(d)
    print(last_item)