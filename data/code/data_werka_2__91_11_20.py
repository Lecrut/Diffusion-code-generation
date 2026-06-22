TRUE_CONSTANT = True
FALSE_CONSTANT = False

class BooleanController:
    def __init__(self, initial_state: bool) -> None:
        self._current_state = initial_state

    def invert_state(self) -> bool:
        if self._current_state:
            self._current_state = FALSE_CONSTANT
        else:
            self._current_state = TRUE_CONSTANT
        return self._current_state

    def retrieve_state(self) -> bool:
        return self._current_state

if __name__ == '__main__':
    controller = BooleanController(TRUE_CONSTANT)
    new_state = controller.invert_state()
    print(new_state)
    current = controller.retrieve_state()
    print(current)