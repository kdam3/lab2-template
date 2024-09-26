#!/usr/bin/env python3

import sys

# Author: Full Kameron Dam
# Author ID: kdam3
# Date Created: 2024/09/25

timer = 10

timer = int(sys.argv[1])

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} timer_number")
    sys.exit(0)


try:
    timer = int(sys.argv[1])
except ValueError:
    print("Error: timer_number must be an integer.")
    sys.exit(1)

if timer < 1:
    print("Error: timer_number must be a positive integer.")
    sys.exit(1)

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
