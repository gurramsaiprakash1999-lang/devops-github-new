from flask import Flask, render_template_string
import platform
import socket
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Civic Pulse | Political & Policy Portal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { background-color: #0b132b; color: #e2e8f0; font-family: 'Segoe UI', sans-serif; }
        .navbar-brand { font-weight: 800; font-size: 1.6rem; background: linear-gradient(135deg, #3b82f6, #ef4444); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .card-custom { background: #1c2541; border: 1px solid #3a506b; border-radius: 12px; transition: all 0.25s ease; }
        .card-custom:hover { transform: translateY(-5px); border-color: #60a5fa; }
        .status-badge { padding: 6px 16px; border-radius: 20px; background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid #3b82f6; }
        .hero-title { font-size: 2.8rem; font-weight: 800; background: linear-gradient(135deg, #60a5fa, #f8fafc, #f87171); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .policy-pill { background: #0b132b; border: 1px solid #3a506b; border-radius: 8px; padding: 14px; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg border-bottom border-secondary mb-4 py-3">
        <div class="container">
            <a class="navbar-brand" href="#"><i class="fa-solid fa-landmark text-primary"></i> CIVIC PULSE</a>
            <span class="status-badge"><i class="fa-solid fa-bullhorn"></i> Public Campaign & Policy Hub</span>
        </div>
    </nav>
    <div class="container pb-5">
        <div class="text-center mb-5">
            <h1 class="hero-title">National Civic & Political Portal</h1>
            <p class="text-light opacity-75 fs-5">Transparent Governance, Legislative Updates & Citizen Engagement</p>
        </div>

        <div class="row g-4 mb-4">
            <div class="col-md-4">
                <div class="card-custom p-4 h-100">
                    <div class="fs-2 text-primary mb-2"><i class="fa-solid fa-scale-balanced"></i></div>
                    <h5 class="text-info fs-6 text-uppercase">Key Policy Focus</h5>
                    <h4 class="fw-bold text-light">Economic & Infrastructure Reform</h4>
                    <p class="mb-0 text-light opacity-75">Public transit expansion, clean energy jobs, and tax transparency.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4 h-100">
                    <div class="fs-2 text-danger mb-2"><i class="fa-solid fa-check-to-slot"></i></div>
                    <h5 class="text-info fs-6 text-uppercase">Voter Participation</h5>
                    <h4 class="fw-bold text-light">Constituency Town Halls</h4>
                    <p class="mb-0 text-light opacity-75">Open public forums and live legislative Q&A sessions every week.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4 h-100">
                    <div class="fs-2 text-warning mb-2"><i class="fa-solid fa-server"></i></div>
                    <h5 class="text-info fs-6 text-uppercase">Portal Node Status</h5>
                    <h4 class="fw-bold text-light">{{ info.ip }}</h4>
                    <p class="mb-0 text-light opacity-75">Host: {{ info.hostname }} | {{ info.time }} UTC</p>
                </div>
            </div>
        </div>

        <div class="card-custom p-4">
            <h5 class="fw-bold text-light mb-3"><i class="fa-solid fa-file-signature text-primary me-2"></i>2026 Legislative Priorities</h5>
            <div class="row g-3">
                <div class="col-md-4">
                    <div class="policy-pill">
                        <strong class="text-info d-block mb-1">1. Digital Public Infrastructure</strong>
                        <span class="small text-light opacity-75">Expanding open-data portals and broadband access across rural districts.</span>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="policy-pill">
                        <strong class="text-info d-block mb-1">2. Healthcare & Education Access</strong>
                        <span class="small text-light opacity-75">Increasing funding for community clinics and vocational skill centers.</span>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="policy-pill">
                        <strong class="text-info d-block mb-1">3. Fiscal Accountability</strong>
                        <span class="small text-light opacity-75">Real-time public budget tracking for municipal and state projects.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def political_portal():
    sys_info = {
        'os': f"{platform.system()} {platform.release()}",
        'hostname': socket.gethostname(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'time': datetime.datetime.now().strftime("%H:%M:%S")
    }
    return render_template_string(HTML_TEMPLATE, info=sys_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
