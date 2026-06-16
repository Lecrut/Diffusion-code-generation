import json
def get_handler(payload):
    decision = payload.get('decision', 'default')
    handlers = {
        'approve': handle_approve,
        'deny': handle_deny,
        'review': handle_review,
        'default': handle_default
    }
    return handlers.get(decision)
def handle_approve(payload):
    user_id = payload.get('user_id', 'unknown')
    amount = float(payload.get('amount', 0))
    print(f"Approving request for {user_id} with amount ${amount}")
def handle_deny(payload):
    reason = payload.get('reason', 'No specific reason provided')
    user_id = payload.get('user_id', 'unknown')
    print(f"Dening request for {user_id}: {reason}")
def handle_review(payload):
    priority = payload.get('priority', 'normal')
    ticket_num = payload.get('ticket_number', 0)
    print(f"Routing to review queue: Ticket #{ticket_num} (Priority: {priority})")
def handle_default(payload):
    message = "Handled with default logic."
    return {"status": "success", "message": message}
if __name__ == '__main__':
    sample_payloads = [
        {'decision': 'approve', 'user_id': 101, 'amount': 500.0},
        {'decision': 'deny', 'reason': 'Credit limit exceeded'},
        {'decision': 'review', 'priority': 'high', 'ticket_number': 998},
        {'decision': 'default'}
    ]
    for payload in sample_payloads:
        try:
            handler = get_handler(payload)
            if callable(handler):
                result = handler(payload)
                print(f"Response from {handler.__name__}:")
            else:
                print(f"Result from {handler.__name__}:", json.dumps(result))
        except Exception as e:
            print(f"Error processing payload: {e}")