# a^(1/e)=b^(1/pi)

import math

res = {}
for a in range(1, 1000):
    b = math.pow(a, math.pi / math.e)
    b_low = math.floor(b)
    b_high = math.ceil(b)
    print(a, b_low, b_high)
    res[(abs(math.pow(a, 1 / math.e) - math.pow(b_low, 1 / math.pi)))] = [a, b_low]
    res[(abs(math.pow(a, 1 / math.e) - math.pow(b_high, 1 / math.pi)))] = [a, b_high]

print(sorted(res.items()))

res = [
    (0.0, [1, 1]),
    (3.4696241435483444e-07, [960, 2797]),
    (5.6748398655770416e-06, [702, 1948]),
    (5.8210297169125624e-06, [888, 2556]),
    (9.626560782294291e-06, [779, 2197]),
    (9.753752060248644e-06, [682, 1884]),
    (9.973868793977658e-06, [949, 2760]),
    (1.0255381337032077e-05, [417, 1067]),
    (1.1322515710787684e-05, [630, 1719]),
    (1.322345777587941e-05, [840, 2397]),
    (1.3319375655740373e-05, [602, 1631]),
    (1.370759928498444e-05, [909, 2626]),
    (1.4197218749956164e-05, [935, 2713]),
    (1.4247376359577402e-05, [912, 2636]),
    (1.94960208652617e-05, [734, 2051]),
    (2.0608916647901765e-05, [891, 2566]),
    (2.213781782423041e-05, [751, 2106]),
    (2.374456845899431e-05, [586, 1581]),
    (2.786198748339075e-05, [499, 1313]),
    (2.890470269534262e-05, [850, 2430]),
    (3.143365461966141e-05, [666, 1833]),
    (3.19367638841328e-05, [398, 1011]),
    (3.401711110306849e-05, [863, 2473]),
    (3.413974448918111e-05, [906, 2616]),
    (3.4440687254111424e-05, [39, 69]),
]
