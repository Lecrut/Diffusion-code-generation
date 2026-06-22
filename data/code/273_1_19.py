MAX_REPETITIONS = 10

def repeat_action(action):
    repetitions = 0
    while repetitions < MAX_REPETITIONS:
        action()
        repetitions += 1

if __name__ == '__main__':
    def sample_action():
        print("Action repeated")
    
    repeat_action(sample_action)