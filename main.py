# student club member checker
from pyscript import display, document


def check_name(e):
    document.getElementById('verify').innerHTML = ' '
    member_name = document.getElementById('name').value
    members = ['Canuday', 'Chua', 'Comanda', 'Lozada', 'Padua', 'Paulino', 'Villante']
    member_checker = member_name in members

    display_message = (f'Sorry {member_name}, you are not part of this club. Try another one.', f'Welcome {member_name}, you are part of the OBMC Math Guild led by Mr. Louise Robin Ferma.')
    
    display(display_message[member_checker], target='verify')