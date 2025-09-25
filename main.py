#whatever
from pyscript import display, document


def ordering_form(e):
    document.getElementById("result").innerHTML = ""
    item1 = document.getElementById("menu1")
    item2 = document.getElementById("menu2")
    item3 = document.getElementById("menu3")
    item4 = document.getElementById("menu4")
    item5 = document.getElementById("menu5")
    item6 = document.getElementById("menu6")
    name = document.getElementById("name1")
    address = document.getElementById("address1")
    phone = document.getElementById("phone1")

    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked + 
             float(item5.value) * item5.checked +
             float(item6.value) * item6.checked)

    display(f'for: {name.value}', target='result')
    display(f'address: {address.value}', target='result')
    display(f'contact: {phone.value}', target='result')
    display(f'the total is {total}', target='result')

