from enum import Enum

class State(Enum):
    START = 1
    PROCESSING = 2
    DONE = 3

def transition(state, event):
    if state == State.START:
        if event == 'BEGIN':
            return State.PROCESSING
    elif state == State.PROCESSING:
        if event == 'END':
            return State.DONE
    return state

if __name__ == '__main__':
    current_state = State.START
    events = ['BEGIN', 'END']
    
    for event in events:
        current_state = transition(current_state, event)
        print(f"Current State: {current_state.name}")