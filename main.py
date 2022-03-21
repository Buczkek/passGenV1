import random
import string


def genPassword(length=8, max_rep=2, char_groups=(string.ascii_lowercase, string.ascii_uppercase, '!@#$%^&*')):
    password = []
    choices = []
    for x in char_groups:
        choices += [x] * max_rep
    last = None
    while len(password) < length:
        temp = random.choice(choices)
        password.append(random.choice(temp))
        choices.remove(temp)
        if temp != last and last:
            n = max_rep - choices.count(last)
            if n != 0:
                choices += [last] * n
        last = temp
    return password


if __name__ == '__main__':
    print(genPassword())
