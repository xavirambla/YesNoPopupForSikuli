#!/usr/bin/python
# -*- coding: UTF-8 -*- 
from javax.swing import JOptionPane;

def YesNoPopup(msg="",title=""):
    result = JOptionPane.showConfirmDialog(None,msg,title,JOptionPane.YES_NO_OPTION);
    if result == JOptionPane.YES_OPTION :
        return True
    else:
        return False

print YesNoPopup(u"¿Desea continuar?", u"Aviso")