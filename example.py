
import json
from zabbix_api import ZabbixAPI


zx = ZabbixAPI(server='http://172.16.198.137/zabbix')

_OUTPUT_PARAMS = {'output': zx.QUERY_EXTEND}


zx.login('Admin', 'zabbix')

# Example: list zabbix users
ret1 = zx.call('user.get', _OUTPUT_PARAMS)
ret2 = zx.user.get({'output': zx.QUERY_EXTEND})

allrest = ret1 + ret2

_UFMT = "%3s  %-8s  %-16s  %-s "


print(_UFMT % ("UID","ALIAS","NAME","SURNAME") )
for user in allrest:
    print(_UFMT % (user["userid"], user["alias"], user["name"], user["surname"]))

#----------------------------------------------------------

_HOSTS = zx.host.get(_OUTPUT_PARAMS)

_HFMT = "%5s  %5s  %-s "

print("= = = = = = = = = = = = = = = = = = = = = = = = ")
print(_HFMT % ("HID", "HPROXY", "HOST") )
for _HOST in _HOSTS:
    #print(json.dumps(_HOST, indent=4))
    print(_HFMT % (_HOST["hostid"], _HOST["proxy_hostid"], _HOST["host"]))

print("= = = = = = = = = = = = = = = = = = = = = = = = ")



#------- HISTORY

# _H_PARAMS = {
#     history: 3,
#     hostids: _HOSTS,

# }
#
# hst = rx.history.get(_H_PARAMS)






#--- Objects examples:

# {
#     "userid": "1",
#     "alias": "Admin",
#     "name": "Zabbix",
#     "surname": "Administrator",
#     "url": "",
#     "autologin": "1",
#     "autologout": "0",
#     "lang": "en_GB",
#     "refresh": "30s",
#     "type": "3",
#     "theme": "default",
#     "attempt_failed": "0",
#     "attempt_ip": "",
#     "attempt_clock": "0",
#     "rows_per_page": "50"
# }


# {
#     "hostid": "10084",
#     "proxy_hostid": "0",
#     "host": "Zabbix server",
#     "status": "0",
#     "disable_until": "0",
#     "error": "",
#     "available": "1",
#     "errors_from": "0",
#     "lastaccess": "0",
#     "ipmi_authtype": "-1",
#     "ipmi_privilege": "2",
#     "ipmi_username": "",
#     "ipmi_password": "",
#     "ipmi_disable_until": "0",
#     "ipmi_available": "0",
#     "snmp_disable_until": "0",
#     "snmp_available": "0",
#     "maintenanceid": "0",
#     "maintenance_status": "0",
#     "maintenance_type": "0",
#     "maintenance_from": "0",
#     "ipmi_errors_from": "0",
#     "snmp_errors_from": "0",
#     "ipmi_error": "",
#     "snmp_error": "",
#     "jmx_disable_until": "0",
#     "jmx_available": "0",
#     "jmx_errors_from": "0",
#     "jmx_error": "",
#     "name": "Zabbix server",
#     "flags": "0",
#     "templateid": "0",
#     "description": "",
#     "tls_connect": "1",
#     "tls_accept": "1",
#     "tls_issuer": "",
#     "tls_subject": "",
#     "tls_psk_identity": "",
#     "tls_psk": "",
#     "proxy_address": "",
#     "auto_compress": "1"
# }






