from Crypto.Util.number import inverse
import binascii

e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

# From factordb

p = 30218956784992282715954619086809201868114195698657276374522212946301458999565770400029957554867011671911288119675964986
q = 30218956784992282715954619086809201868114195698657276374522458787537971478418523309764870130448827639541321169514234070

phi = (p-1) * (q-1)

d = inverse(e,phi)
m = pow(c,d,n)

hex_str = hex(m)[2:] # Removing '0x'
print(binascii.unhexlify(hex_str))