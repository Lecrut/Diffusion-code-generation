def repeat_sequence(action):
    for _ in range(5):
        action()

if __name__ == '__main__':
    def sample_action():
        print("Action repeated")
    
    repeat_sequence(sample_action)