#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])  # Print an empty list
        return
    elif length == 1:
        print([0])  # Print [0] for length 1
        return
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    print(fib_sequence)
