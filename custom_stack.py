def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    openings = set(pairs.values())
    closings = set(pairs.keys())

    for ch in s:
        if ch in openings:
            stack.append(ch)
            continue

        if ch in closings:
            if not stack:
                return False
            if stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0
