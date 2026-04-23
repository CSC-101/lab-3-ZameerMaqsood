#Task 1
more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step. -- 1+1, 2+1, 3+1, 4+1,
print()                               # What is the value of more at this point? [2, 3, 4, 5]

def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value. [1,4,9,16]


squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above? [1,4,9,16]--- same values

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. 1,2,3,4-->False,False,True,True


answer = [x for x in range(5) if check(x)]   # What is the value of answer? [3,4]
print()


def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value. [3+1, 4+1]--> [4,5]


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and [False, False, False, True, True]
                                             # the corresponding return value. [3,4]


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4,5]
print()


#Task 2
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
    return total                      # 0+4-->4+9-->13+2-->15+1--> 16

result = tally([4, 9, 2, 1])
def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.[4,9,2,1]
    return new_list                    # How does this loop differ from that above? Rewrites list rather than summing

result = copy([4, 9, 2, 1])
def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. [5,10,3,2]
    return new_list

