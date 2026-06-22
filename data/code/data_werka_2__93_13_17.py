from enum import Enum

class BooleanState(Enum):
    FALSE = 0
    TRUE = 1

class LogicGate:
    _states = {
        False: BooleanState.FALSE,
        True: BooleanState.TRUE
    }
    
    @staticmethod
    def _to_state(val: bool) -> BooleanState:
        return LogicGate._states[val]

    @staticmethod
    def _is_false(state: BooleanState) -> bool:
        return state is BooleanState.FALSE

    @staticmethod
    def check_both_false(a: bool, b: bool) -> bool:
        state_a = LogicGate._to_state(a)
        state_b = LogicGate._to_state(b)
        
        a_false = LogicGate._is_false(state_a)
        b_false = LogicGate._is_false(state_b)
        
        return a_false and b_false

if __name__ == '__main__':
    val_a = False
    val_b = False
    result = LogicGate.check_both_false(val_a, val_b)
    print(result)
    
    val_c = True
    val_d = False
    result2 = LogicGate.check_both_false(val_c, val_d)
    print(result2)