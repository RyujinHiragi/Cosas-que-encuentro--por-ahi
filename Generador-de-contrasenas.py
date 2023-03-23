import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numers = "0123456789"

all = lower + upper + numers
length = 16
password = "". join(random.sample(all,length))

print(password)
