import string
import random

karakteret = list(string.ascii_letters + string.digits + "ëç!@#$%^&*()")


def gjenero_fjalekalim_random():
    gjatesia = int(input("Shkruani gjatesine e fjalekalimit: "))

    random.shuffle(karakteret)

    fjalekalim = []
    for i in range(gjatesia):
        fjalekalim.append(random.choice(karakteret))

    random.shuffle(fjalekalim)

    print("".join(fjalekalim))


gjenero_fjalekalim_random()
