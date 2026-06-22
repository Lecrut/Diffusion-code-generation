import time

def repeat_sequence(action_func):
    actions = {
        'print_action': action_func,
        'delay_time': 2,
        'repeat_count': 5
    }
    
    for _ in range(actions['repeat_count']):
        actions['print_action']()
        time.sleep(actions['delay_time'])

if __name__ == '__main__':
    def sample_action():
        print('Action executed')
    
    repeat_sequence(sample_action)