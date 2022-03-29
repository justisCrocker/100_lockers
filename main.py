# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def unique_factors(num):
    """Calculates how many unique factors a given integer has.

    :param num: int Number to find factors for
    :return: int Number of unique factors
    """
    # Edge case: when num is 1, it is immediately obvious that the number of unique factors is 1
    if num == 1:
        return 1
    # result will be incremented for each unique factor found
    result = 2
    # range doesn't include with 1 because 1 and num are always factors (already counted above)
    # range also doesn't include anything above half of num, as those could never be factors
    for x in range(2, num // 2 + 1):
        if num % x == 0:
            result += 1
    return result


def lockers():
    """Calculates the number of open lockers in 100 Lockers problem

    :return: int Number of open lockers
    There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers.
    Next, he closes every second locker. Then, on his third pass, he toggles every third locker
    (closes it if it is open or opens it if it is closed). This process continues for 100 passes,
    such that on each pass 'i', the man toggles every 'i'th locker. After his 100th pass in the hallway,
    in which he toggles only locker #100, how many lockers are open?
    """
    # Make a list of 101 True booleans
    # First index ignored to pretend index starts at 1
    lock_list = [True for x in range(101) if x == x]
    # result variable acts as an incremented counter for open lockers
    result = 0
    # loops on indexes of lock_list and evaluates if that locker is open at the end of 100 passes
    # This is sped up by realizing that a locker will be open if it was toggled an odd number of times.
    # (means that program only needs to loop through the list once, not 100 times!)
    # Each door is toggled once for every unique factor it's index has
    # (first pass toggle divisible by 1, second pass toggle divisible by 2, third pass toggle divisible by 3, etc...)
    for i in range(len(lock_list)):
        if i >= 1 and unique_factors(i) % 2 != 0:
            result += 1
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(lockers())
