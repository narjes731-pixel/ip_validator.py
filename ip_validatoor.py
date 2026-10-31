import ipaddress

print("Welcome to IP Address Validator!")

ip = input("Enter an IPv4 address: ")

try:
    address = ipaddress.IPv4Address(ip)

    print("Valid IPv4 address!")

    if address.is_private:
        print("This is a private IP address.")
    else:
        print("This is a public IP address.")

except ipaddress.AddressValueError:
    print("Invalid IPv4 address!")
