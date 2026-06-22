MAX_ITERATIONS = 5

def repeat_sequence(action):
    for _ in range(MAX_ITERATIONS):
        action()

if __name__ == '__main__':
    def sample_action():
        print("Action repeated")
    
    repeat_sequence(sample_action)